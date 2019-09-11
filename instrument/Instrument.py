import pandas as pd
import numpy as np


class Single_Asset_Instrument:
	"""
	Single_Asset_Instrument serves as a data classification system for any other upper-level class. It classifies raw data into different
	categories. 
	Each categories might include specific attributes that only belongs to the asset class itself.
	If any upper level class needs to access data, it should use one of the single asset instrument.

	"""

	def __init__(self,instru_class,ticker,date,price,ret):
		"""
		This class has three general attributes shared by all specific instruments.

		Attributes:
		------------
		ticker: str, the name of the instrument
		instrument_class: str, the class of the instrument
		date: pd.Series, the date of the data
		"""

		self.ticker = ticker
		self.instrument_class = instru_class
		self.date = pd.to_datetime(date)
		self.price = price
		ret.index = self.date
		self.ret = ret

	def get_instrument_class(self):
		"""
		This function prints the type of the instrument.

		:nreturn:
		"""
		print(self.instrument_class)

	def get_ticker(self):
		"""
		This function prints the name of the instrument.

		:nreturn:

		"""
		print(self.ticker)




class Asset(Single_Asset_Instrument):
	"""
	One type of single series instrument. 
	It stores specific information related to one single asset

	"""

	def __init__(self,ticker,date,price,ret):
		Single_Asset_Instrument.__init__(self,"Asset",ticker,date,price,ret)




class Hedge_Fund(Single_Asset_Instrument):
	"""
	One type of single asset instrument, Hegde Fund.
	It store specific information related to the hedge fund.



	"""

	def __init__(self,ticker,date,price,ret,AUM):
		"""
		Currently, it has one specific attribute, AUM.

		Attributes:
		------------
		AUM: pd.Series(float)

		"""
		Single_Asset_Instrument.__init__(self,"Hedge Fund",ticker,date,price,ret)
		self.AUM = AUM




class Multiple_Asset_Instrument:
	"""
	This class is used to store multiple single series instruments in an organized way. 
	The specific way is tailored for different type of analysis purpose.

	"""

	def __init__(self,ticker_list,instru_dic,date):
		"""
		This class has three general attributes shared by all specific instruments.

		Attributes:
		------------
		ticker_list: list(str), list of name of the assets
		performance_list: dict(Asset), it contains the single asset instrument in the portfolio.
		date: pd.Series, the date of the data
		"""

		self.ticker_list = ticker_list
		self.performance = instru_dic
		self.instrument_class = None
		self.date = pd.to_datetime(date)



	def get_all_instruments_name(self):
		"""
		This function prints the name of each single series instrument stored in this multiple series instrument.

		:nreturn:

		"""

		for ticker in self.ticker_list:
			print(ticker+"\n")


	def get_certain_instrument(self,ticker):
		"""
		This function returns certain instrument stored in the multiple instrument.

		:return: Single_Asset_Instrument

		"""

		return self.performance[ticker]
	




class Portfolio(Multiple_Asset_Instrument):
	"""
	One type of multiple assets instrument, portfolio.
	This instrument is used to store the information about certain portfolio.
	This instrument is designed for portfolio with no rebalance. 
	If rebalance is needed, a new instrument should be initialized.

	"""

	def __init__(self,ticker_list,instru_dic,ini_weight,date):
		"""
		This class has specific attribute, ini_weight.

		Attributes:
		------------
		weight: list(float), the number of initial holding of each asset

		"""
		Multiple_Asset_Instrument.__init__(self,ticker_list,instru_dic,date)

		self.weight = ini_weight
		self.instrument_class = "Portfolio"

	########################################################
	######### Attribute Information Extraction #############
	########################################################



	def weight_update(self,new_ini_weight):
		"""
		This function is used to update the weight of each asset in the portfolio.

		:nreturn:
		"""
		self.weight = new_ini_weight
		print("Portfolio Weight is updated.")



	########################################################
	############## Other Relevant Methods ##################
	########################################################


	def empirical_weight(self):
		"""
		This function calculates the empirical weight measured by proportion of 1 dollar invested in the portfolio
		at certain time.

		:return: list(float)

		"""
		pass




	def portfolio_performance(self):
		"""
		This function calcualtes the performance of the portfolio during the period.

		:return: pd.Series


		"""
		pass

		


class TermStructure(Multiple_Asset_Instrument):
	"""
	One type of multiple asset instrument, Term structure.
	This class is used to store certain term structure information.

	"""

	def __init__(self,ticker_list,instru_dic,maturity,date):
		"""
		This class has specific attribute, maturity

		Attributes:
		------------
		maturity: list(float)

		"""
		Multiple_Asset_Instrument.__init__(self,ticker_list,instru_dic,date)

		self.maturity = maturity
		self.instrument_class = "Term Structure"




































