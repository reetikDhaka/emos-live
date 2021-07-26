
//declaration of variables
const empName = document.getElementById('employee-name');
const empEmail = document.getElementById('email');
const empPhone = document.getElementById('phone-number');
//form validators
//name validator

//email validator
empEmail.addEventListener('change', function(){
    const div = document.querySelector('.errormail')
    if (empEmail.value.match('@')){
        div.style.display = 'none'; 
       }
       else{
           div.innerHTML = "please enter a valid email";
       }
    
})
//phone-number validator
empPhone.addEventListener('change',function(){
    const div = document.querySelector('.errorphone')
    if(empPhone.value.length!=10){
        div.innerHTML = "please enter a valid phone number";
    }
    else{
        div.style.display = 'none';
    }
})


//functions

