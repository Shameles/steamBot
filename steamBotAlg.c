//steanBotAlgorithm

#define CSGO_FEE 10
#define STEAM_FEE 5
#define BUY_MARGIN 20
#define PROFIT_MARGIN 10

char priceArray = [];
double lowestListedPrice = import.steam.priceLow
int marketQuantity = import.steam.quantity;

int buy(char priceArray, double lowestListedPrice, int marketQuantity){
	int averagePrice = arrayTotal(priceArray)/arrayCount(priceArray);
	int storeItemPrice;
	if(lowestListedPrice  <= averagePrice - (averagePrice * 0.BUY_MARGIN)){
		storeItemPrice = averagePrice - (averagePrice * 0.BUY_MARGIN);
		execute.steam.buy.item(lowestListedPrice);
	}
	return storeItemPrice;
}

void sell(int storeItemPrice){
	execute.steam.sell.item(storeItemPrice * (0.CSGO_FEE + 0.STEAM_FEE + 0.PROFIT_MARGIN));
}

int arrayTotal(char priceArray){
	int i;
	int total =0;
	for(i=0;priceArray[i] != '/0';i++){
		total = total + priceArray[i];
	}
	return total;
}

int arrayCount(char priceArray){
	int i;
	int total =0;
	for(i=0;priceArray[i] != '/0';i++){
		total++; 
	}
	return total;
}
