import argparse
import datetime
import pyiqfeed as iq # https://github.com/akapur/pyiqfeed.git
import time
import numpy as np

np.set_printoptions(threshold=np.inf)

dtn_product_id = "JUNDONG_CHEN_#####"
dtn_login = "5037##"
dtn_password = "Cjd###########"

def launch_service():
    svc = iq.FeedService(product=dtn_product_id, version="Debugging", login=dtn_login, password = dtn_password)
    svc.launch(headless=False)

def get_level_1_quotes_and_trades(ticker: str, seconds: int):
    quote_conn = iq.QuoteConn(name="pyiqfeed-lvl1")
    quote_listener = iq.VerboseQuoteListener("Level 1 Listener")
    quote_conn.add_listener(quote_listener)

    with iq.ConnConnector([quote_conn]) as connector:
        all_fields = sorted(list(iq.QuoteConn.quote_msg_map.keys()))
        quote_conn.select_update_fieldnames(all_fields)
        quote_conn.watch(ticker)
        time.sleep(seconds)
        quote_conn.unwatch(ticker)
        quote_conn.remove_listener(quote_listener)

def get_tickdata(ticker: str, max_ticks: int, num_days: int):
    hist_conn = iq.HistoryConn(name="pyiqfeed-tickdata")
    hist_listener = iq.VerboseIQFeedListener("History Tick Listener")
    hist_conn.add_listener(hist_listener)

    with iq.ConnConnector([hist_conn]) as connector:
        try:
            # Get the last num_days days trades between 10AM and 12AM
            # Limit to max_ticks ticks else too much will be printed on screen
            bgn_flt = datetime.time(hour=9, minute=30, second=0)
            end_flt = datetime.time(hour=9, minute=35, second=0)
            tick_data = hist_conn.request_ticks_for_days(ticker=ticker, num_days=num_days, bgn_flt=bgn_flt, end_flt=end_flt, max_ticks=max_ticks)
            print(tick_data)
        except (iq.NoDataError, iq.UnauthorizedError) as err:
            print("No data returned because {0}".format(err))

def get_equity_option_chain(ticker: str):
    lookup_conn = iq.LookupConn(name="pyiqfeed-Eq-Option-Chain")
    lookup_listener = iq.VerboseIQFeedListener("EqOptionListener")
    lookup_conn.add_listener(lookup_listener)
    with iq.ConnConnector([lookup_conn]) as connector:
        e_opt = lookup_conn.request_equity_option_chain(
            symbol = ticker,
            opt_type = 'pc',
            month_codes = "".join(iq.LookupConn.call_month_letters + iq.LookupConn.put_month_letters),
            near_months = None,
            include_binary = True,
            filt_type = 2,
            filt_val_1 = 1,
            filt_val_2 = 1,
        )
        print(f"Currently trading options for {ticker}")
        print(e_opt)
        lookup_conn.remove_listener(lookup_listener)

def get_news(ticker: str):
    news_conn = iq.NewsConn("pyiqfeed-News-Conn")
    news_listener = iq.VerboseIQFeedListener("NewsListener")
    news_conn.add_listener(news_listener)
    with iq.ConnConnector([news_conn]) as connector:
        print("Latest 10 headlines:")
        headlines = news_conn.request_news_headlines(
            sources=[], symbols=[], date=None, limit=10)
        print(headlines)
        print("")

        story_id = headlines[0].story_id
        story = news_conn.request_news_story(story_id)
        print("Text of story with story id: %s:" % story_id)
        print(story.story)
        print("")


if __name__ == "__main__":
    launch_service()
    #get_level_1_quotes_and_trades(ticker="SPY", seconds=30)
    #get_tickdata(ticker="SPY", max_ticks=np.inf, num_days=1)
    #get_equity_option_chain("BA")
    #get_news("AAPL")
