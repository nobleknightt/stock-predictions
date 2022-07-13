import streamlit as st
import yfinance as yf

from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from pandas import DataFrame

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

@st.cache
def load_data(ticker: str) -> DataFrame:
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

def plot_raw_data(data: DataFrame, selected_stock: str) -> None:
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data["Date"], y=data["Open"], name="Opening Price")
    )
    fig.add_trace(go.Scatter(
        x=data["Date"], y=data["Close"], name="Closing Price")
    )
    fig.update_layout(
        title_text=f"Stock Prices (USD) for {selected_stock}",
        xaxis_rangeslider_visible=True,
        xaxis_title_text="Time Stamp",
        yaxis_title_text="Price (USD)",
        height=500, width=800
    )
    st.plotly_chart(fig)

def main():

    st.set_page_config(
        page_title="Stock Prediction App",
        page_icon=":chart_with_upwards_trend:"    
    )

    st.title("Stock Prediction App")

    stocks = {
        "Apple Inc. (AAPL)" : "AAPL",
        "Microsoft Corporation (MSFT)" : "MSFT",
        "Twitter, Inc. (TWTR)" : "TWTR",
        "Tesla, Inc. (TSLA)" : "TSLA",
        "Alphabet Inc. (GOOG)" : "GOOG", 
        "Meta Platforms, Inc. (META)" : "META"
    }

    selected_stock = st.selectbox("Select Stock for Prediction", list(stocks.keys()))

    n_years = st.slider("Years of Prediction", 1, 5)
    periods = n_years * 365

    data_load_state = st.text("Loading Data ...")
    data = load_data(stocks[selected_stock])
    data_load_state.text("Loading Data ... Done!")

    st.subheader("Stock Prices")
    # st.write(data.tail())

    plot_raw_data(data, selected_stock)

    training_data = data[["Date", "Close"]]

    # https://facebook.github.io/prophet/docs/quick_start.html#python-api
    # the input to prophet is always a dataframe with two columns: ds and y
    training_data.rename(columns={
        "Date": "ds", "Close": "y"
    }, inplace=True)

    model = Prophet()
    model.fit(training_data)

    future = model.make_future_dataframe(periods=periods)
    predictions = model.predict(future)

    st.subheader("Predictions")

    # st.write(predictions.tail())

    fig1 = plot_plotly(model, predictions)

    fig1.update_layout(
        title_text=f"Prediction for {selected_stock}",
        xaxis_title_text="Time Stamp",
        yaxis_title_text="Price (USD)",
        showlegend=True
    )

    fig1_data = fig1.to_dict()

    fig1_data["data"][1]["name"] = "Prediction Lower Bound"
    fig1_data["data"][3]["name"] = "Prediction Upper Bound"

    del fig1_data["layout"]["xaxis"]["rangeselector"]

    st.plotly_chart(fig1_data)

    # st.subheader("Prediction Components")
    # fig2 = model.plot_components(predictions)
    # st.write(fig2)

if __name__ == "__main__":

    main()