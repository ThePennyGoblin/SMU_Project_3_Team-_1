import numpy as np
import plotly.express as px
from src.app.db_operations import query_metrics, query_specs
from src.config.config import HIST_CONFIG

def generate_histogram(product_name, engine, config_key):
   
   plot_configurations = HIST_CONFIG[config_key]
   
   m_df = query_metrics(engine, product_name)
   s_df = query_specs(engine, product_name)
   
   bin_edges = get_bins(m_df, plot_configurations)
   posts = goal_posts(s_df, m_df, plot_configurations)
   
   return make_plot(m_df, bin_edges, posts, plot_configurations[0], .25)
   
   
def get_bins(metric_df, config):
   col = config[0]
   bin_min = np.floor(metric_df[col].min()) - 1
   bin_max = np.ceil(metric_df[col].max()) + 1
   bin_edges = (bin_min, bin_max)
   return bin_edges

def goal_posts(spec_df, metric_df, config):
   
   min_goal = spec_df[config[1]].values[0]
   max_goal = spec_df[config[2]].values[0]
   avg_goal = round(metric_df[config[0]].mean(), 3)
   posts =  (min_goal, max_goal, avg_goal)
   return posts

def make_plot(df, bins, posts, col, step):
   
   fig = px.histogram(df, x=col)
   fig.add_vline(x=posts[0], line_dash='solid', line_color='red',annotation_text=f"{posts[0]:.2f}", annotation_position="top left")
   fig.add_vline(x=posts[1], line_dash='solid', line_color='red',annotation_text=f"{posts[1]:.2f}", annotation_position="top left")
   fig.add_vline(x=posts[2], line_dash='longdash', line_color='blue',annotation_text=f"{posts[2]:.2f}", annotation_position="top left")

   fig.update_layout(
      width=800,
      height=600,
      title=f'Histogram of {col} with Goals',
      xaxis_title=f'{col}',
      yaxis_title='Count',
   )

   fig.update_traces(marker=dict(color='#43A7E5', line=dict(width=1, color='DarkSlateGrey')))

   fig.update_traces(xbins=dict(
      start=bins[0],
      end=bins[1],
      size=step
   ))
   fig.show()
   # return fig
   