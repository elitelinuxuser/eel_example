function generateQRCode() {
	var data = document.getElementById("data").value
	var newData = document.getElementById("newbox");
	var finalData = eel.getWeather(data)
	newData.value = finalData;

}

function setimage(info){
	//prompt("the temperature is" +info)
}
