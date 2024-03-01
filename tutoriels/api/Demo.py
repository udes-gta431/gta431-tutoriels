# Importation des modules
import yfinance as yf

# Actions qui nous intéressent
tickers = (
    "AAPL",  # Apple
    "MSFT",  # Microsoft
)

#Récupération des données
for ticker in tickers:
    action = yf.Ticker(ticker)

    # Informations générales
    print(action.info["longBusinessSummary"])  # Description de l'entreprise
    print(action.info["marketCap"])  # Capitalisation boursière
    print(action.recommendations)  # Recommandations des analystes

    # Données historiques
    period = "2y"  # Période en jours (d), semaines (wk), mois (mo), années (y) ou autre (YTD, max)
    value = ("Close")  # Valeurs acceptées : "Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"

    print(action.history(period=period)[value])
