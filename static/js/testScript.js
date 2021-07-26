const submitbtn = document.querySelector('submitbtn');
const alertpanel = document.querySelector('panel');
const username = document.getElementById('name')
username.addEventListener('change',function(){
    let letters = /^[A-Za-z]+$/;
    if(username.value.match(letters)){
       console.log('fine')    
    }
    else{
        const div = document.querySelector('.error')
        div.innerHTML = 'name cannot contains numbers';

        console.log('workinh')
    }

})

