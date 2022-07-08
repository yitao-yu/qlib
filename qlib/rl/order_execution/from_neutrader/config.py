from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Tuple, Union


@dataclass
class ExchangeConfig:
    limit_threshold: Union[float, Tuple[str, str]]
    deal_price: Union[str, Tuple[str, str]]
    volume_threshold: dict
    open_cost: float = 0.0005
    close_cost: float = 0.0015
    min_cost: float = 5.0
    trade_unit: Optional[float] = 100.0
    cash_limit: Optional[Union[Path, float]] = None
    generate_report: bool = False
