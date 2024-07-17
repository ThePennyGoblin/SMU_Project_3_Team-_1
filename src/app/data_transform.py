import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
import plotly.express as px

def get_bins(metric_df, product_name):
   current_product = metric_df.loc[metric_df['product_name'] == product_name]
    
   bin_min = np.floor(current_product['measured_weight'].min())-1
   bin_max = np.ceil(current_product['measured_weight'].max())+1

   bin_edges = (bin_min, bin_max)
   return bin_edges

def goal_posts(spec_df, metric_df, product_name):
   
   spec_product = spec_df.loc[spec_df['product_name'] == product_name]
   metric_product = metric_df.loc[metric_df['product_name'] == product_name] 
   
   min_goal = spec_product['weight_min'].values[0]
   max_goal = spec_product['weight_max'].values[0]
   avg_goal = round(metric_product['measured_weight'].mean(), 3)
   
   posts =  (min_goal, max_goal, avg_goal)
   return posts

def query_metrics(engine, product_name):
   query = f""" 
   Select measured_weight, measured_height from metrics where product_name = {product_name};   
   """
   df = pd.read_sql(query=query,engine=engine)
   return df
      
      
def query_specs(engine, product_name):
   query = f""" 
   Select weight_min, weight_max, height_min, height_max from specs where product_name = {product_name};   
   """
   df = pd.read_sql(query=query,engine=engine)
   return df


def make_plot(df, bins, posts, col, step):
   
   fig = px.histogram(df, x=col)
   fig.add_vline(x=posts[0], line_dash='solid', line_color='red',annotation_text=f"{posts[0]:.2f}", annotation_position="top left")
   fig.add_vline(x=posts[1], line_dash='solid', line_color='red',annotation_text=f"{posts[1]:.2f}", annotation_position="top left")
   fig.add_vline(x=posts[2], line_dash='longdash', line_color='blue',annotation_text=f"{posts[2]:.2f}", annotation_position="top left")

   fig.update_layout(
      width=800,
      height=600,
      title='Histogram of Measured Weight with Goals',
      xaxis_title='Measured Weight',
      yaxis_title='Count',
   )

   fig.update_traces(marker=dict(color='#43A7E5', line=dict(width=1, color='DarkSlateGrey')))

   fig.update_traces(xbins=dict(
      start=bins[0],
      end=bins[1],
      size=step
   ))
   fig.show()
   
# fig.add_vline(x=height_avg, line=dict(color="green", width=3), annotation_text=f"{height_avg:.2f}", annotation_position="top left")
# fig.add_vline(x=height_min_spec, line=dict(color="red", width=2, dash='dash'), annotation_text=f"{height_min_spec:.2f}", annotation_position="top left")
# fig.add_vline(x=height_max_spec, line=dict(color="red", width=2, dash='dash'), annotation_text=f"{height_max_spec:.2f}", annotation_position="top left")
