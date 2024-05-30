from pydantic import BaseModel
from typing import Optional

class Pair(BaseModel):
    id: str
    base_currency: str
    quote_currency: str
    quote_increment: str
    base_increment: str
    display_name: str
    min_market_funds: str
    margin_enabled: bool
    post_only: bool
    limit_only: bool
    cancel_only: bool
    status: str
    status_message: str
    trading_disabled: bool
    fx_stablecoin: bool
    max_slippage_percentage: str
    auction_mode: bool
    high_bid_limit_percentage: Optional[str]  # Optional field

class Pairs(BaseModel):
    base: list[Pair]
