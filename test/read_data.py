import pandas as pd
from src.main import IncreaseProfitSixthCampaign


def test_read_csv():

    test_increase_profit_sixth_campaign = IncreaseProfitSixthCampaign()

    assert test_increase_profit_sixth_campaign.read_csv() == True
