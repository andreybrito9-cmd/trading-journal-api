from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Trading Journal API",
    description="API demo to manage and analyze trading operations.",
    version="1.0.0"
)

class Trade(BaseModel):
    symbol: str
    direction: str
    entry_price: float
    exit_price: float
    profit: float

trades: List[Trade] = []

@app.get("/")
def home():
    return {"message": "Trading Journal API is running"}

@app.post("/trades")
def create_trade(trade: Trade):
    trades.append(trade)
    return {"message": "Trade saved successfully", "trade": trade}

@app.get("/trades")
def get_trades():
    return trades

@app.get("/stats")
def get_stats():
    total_trades = len(trades)
    total_profit = sum(trade.profit for trade in trades)
    winning_trades = len([t for t in trades if t.profit > 0])
    losing_trades = len([t for t in trades if t.profit < 0])
    winrate = (winning_trades / total_trades * 100) if total_trades else 0

    return {
        "total_trades": total_trades,
        "total_profit": total_profit,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "winrate": round(winrate, 2)
    }