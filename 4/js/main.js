function reverseString(produto) {
	var pString = produto.toString();
	var reversedString = "";
		for (var i = 0; i < pString.length; i++) {
		reversedString += pString[pString.length-i-1];	
	}
	return reversedString;
}

function checkPalindrom(produto) {
	return produto.toString() == reverseString(produto);
}

function helper(p, l) {
	if (!checkPalindrom(p)){
		return l;
	}
	if (p >= l) {
		return p;
	}
	return l;
}

function solve(){
	var l = 0;
	for (var i = 0; i < 1000; i++){
		for (var k = 0; k < 1000; k++){
			var p = k * i;
			l = helper(p, l);
		}
	}
	return l;
}

console.log(solve());
