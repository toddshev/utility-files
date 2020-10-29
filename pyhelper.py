 
 #work in progress
 
 #to be used with pandas
 class Finhelper: #fin helper
    def __init__():
      pass
        def load_and_clean(in_path):
            df = pd.read_csv(in_path, index_col = 0, parse_dates = True, infer_datetime_format = True)
            df.dropna(inplace = True)
            df.drop_duplicates(inplace = True)
            return df

        def get_cov(df, tick, ind):
            #return covariance from dataframe, ticker, and index
            cov= df[tick].cov(df[ind])
            return cov
    
        def get_corr(df):
            return df.corr()
        
        def get_beta(df,tick,ind):
            #get beta from dataframe, ticker, and index, uses get_cov
            cov = get_cov(df,tick,ind)
            var = df[ind].var()
            beta = cov / var
            return beta

        def get_sharpe(df, df_type):
            #df_type should be either "price" or "returns" based on dataframe passed in
            if df_type == "price":
                df = df.pct_change(inplace = True)
            sharpe = (df.mean() * 252) / (df.std() * np.sqrt(252))
            return sharp
        
        def get_volatility(df):
            #annualized standard deviation
            return df.std() * np.sqrt(252)
        
        def allocate(weights, df):
            #weighted portfolio, weights must be a list of same count as assets
            return df.dot(weights)
        
        def get_cum_returns(df, init_inv = 1):
            #dataframe must be daily_returns.  Optional investment amount as 2nd arg
            return ((1 + df).cumprod()) * init_inv
        
        def drop():
            #returns help text...thought I'd try this out
            return f"dataframe.drop(columns=['column1', 'column2', 'column3'], inplace=True)"
            #return "Hello"
        def get_rolling(df, days):
            #returns rolling average
            return df.rolling(window=days).mean()
            
class SQLhelper:
    def __init__():
        pass
        
    def create():
        return "CREATE TABLE <tablename> ( \n"
               "    <field1> SERIAL PRIMARY KEY,\n"
               "    <field2> INT,\n"
               "    <field3> DOUBLE PRECISION,\n"
               "    <field4> FLOAT(10)\n"
               ");"
