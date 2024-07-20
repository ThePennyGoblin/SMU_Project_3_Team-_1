import numpy as np
import plotly.express as px
from src.app.db_operations import query_metrics, query_specs
from src.config.config import HIST_CONFIG, OUTLIERS_CONFIG

def generate_histogram(product_name, engine, config_key):
   
   plot_configurations = HIST_CONFIG[config_key]

   m_df = query_metrics(engine, product_name)

   # transform > 50 weights as those are obvious outliers. 
   m_df = normalize_outliers(m_df, OUTLIERS_CONFIG['col'], OUTLIERS_CONFIG['outlier'])

   s_df = query_specs(engine, product_name)
   
   num_bins = get_bins(m_df, plot_configurations)
   posts = goal_posts(s_df, m_df, plot_configurations)
   
   return make_plot(m_df, num_bins, posts, plot_configurations[0], product_name, config_key, plot_configurations[4])
   
   
def normalize_outliers(df, col, outlier):
   """normalizes uppler outliers of weight.
   Returns:
   """
   df[col] = df[col].apply(lambda x: x * 0.01 if x > outlier else x)
   return df


def get_bins(metric_df, config):
   col = config[0]
   step = config[3]
   bin_min = np.floor(metric_df[col].min()) - 1
   bin_max = np.ceil(metric_df[col].max()) + 1
   bin_difference = bin_max - bin_min
   num_of_bins = int(bin_difference * 1/step)
   return num_of_bins

def goal_posts(spec_df, metric_df, config):
   
   min_goal = spec_df[config[1]].values[0]
   max_goal = spec_df[config[2]].values[0]
   avg_goal = round(metric_df[config[0]].mean(), 3)
   posts =  (min_goal, max_goal, avg_goal)
   return posts

def make_plot(df, bins, posts, col, prod_name, type_of_chart, axis_labels):
   fig = px.histogram(df, x=col, nbins=bins)
   fig.add_vline(x=posts[0], line_dash='solid', line_color='red', line_width=4, annotation_text=f"{posts[0]:.2f}", annotation_position="top left")
   fig.add_vline(x=posts[1], line_dash='solid', line_color='red', line_width=4, annotation_text=f"{posts[1]:.2f}", annotation_position="top left")
   fig.add_vline(x=posts[2], line_dash='longdash', line_color='blue', line_width=4, annotation_text=f"{posts[2]:.2f}", annotation_position="top left")
     # Add invisible scatter points for legend
   fig.add_scatter(x=[None], y=[None], mode='lines', line=dict(color='red', dash='solid'), name=f"Spec Min {posts[0]:.2f}")
   fig.add_scatter(x=[None], y=[None], mode='lines', line=dict(color='red', dash='solid'), name=f"Spec Max {posts[1]:.2f}")
   fig.add_scatter(x=[None], y=[None], mode='lines', line=dict(color='blue', dash='longdash'), name=f"Mean {posts[2]:.2f}")
   fig.update_layout(
      autosize=True,
      title=f'{type_of_chart.capitalize()} Distribution of {prod_name}',
      xaxis_title=f'{axis_labels}',
      yaxis_title='Count',
      plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
      paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
      font=dict(color='lightgrey')
   )
   fig.update_xaxes(showline=True, linewidth=2, linecolor='grey', gridcolor='grey')
   fig.update_yaxes(showline=True, linewidth=2, linecolor='grey', gridcolor='grey')
   fig.update_traces(marker=dict(color='#5BC0DE', line=dict(width=1, color='DarkSlateGrey')))
   
   return fig