const month_array = new Array();
month_array[1]='January';
month_array[2]='February';
month_array[3]='March';
month_array[4]='April';
month_array[5]='May';
month_array[6]='June';
month_array[7]='July';
month_array[8]='August';
month_array[9]='September';
month_array[10]='October';
month_array[11]='November';
month_array[12]='December';

let today = new Date();
let date = today.getDate()+'-'+month_array[today.getMonth()+1]+'-'+today.getFullYear();
let current_hour = today.getHours()
const greeting = document.querySelector('.greetings')
const header = document.querySelector('.date');
header.innerHTML = date;
if (current_hour<12){
    greeting.innerHTML = "Good Morning,";
}
else if(12<current_hour<16){
    greeting.innerHTML = "Good AfterNoon,";
}
else{
    greeting.innerHTML = 'Good Evening';
}