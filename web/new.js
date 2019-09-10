function generateQRCode() {
	var data = document.getElementById("data").value;
	// console.log(eel.getWeather(data)(setData))
	eel.getWeather(data)(setData)

}

const setUser = ()=>{
	var data = document.getElementById("data").value;
	eel.getUser(data);
}

function setData(info){
	var newData = document.getElementById("newbox");
	newData.innerHTML = info;    
}