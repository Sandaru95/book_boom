function contact_print(){
	window.alert('Contact Details:\nMail: nishanthapubli@gmail.com\nTel: +94112247436\n For Further Details Visit Our Contact Page');
}
function verify_login(){
	let userName = document.getElementById('username').value;
	let password = document.getElementById('password').value;

	if (userName == '' && password == ''){
		window.alert("There's something wrong with the credentials entered. Check them and try again!");
	}
}