//declaration of elements
const approveBtn = document.getElementsByClassName('approve');
const modal = document.getElementsByClassName('confirm-modal')
const finalapprovalBtn = document.getElementsByClassName('approveEmp');
const closeBtn = document.getElementsByClassName('close');
const viewApplicationBtn = document.getElementsByClassName('view-app');
const applicationModal = document.getElementsByClassName('application-modal');
const appCloseBtn = document.getElementsByClassName('close-app');
//loops for multiple buttons
for (let i=0;i<approveBtn.length;i++){
    approveBtn[i].addEventListener('click',()=>modal[i].style.display='block');
    window.addEventListener('click',function(e){
        if(e.target==modal[i]){
            modal[i].style.display = "none";
        }
    })
    
    closeBtn[i].addEventListener('click',()=>modal[i].style.display="none");
    finalapprovalBtn[i].addEventListener('click',function(){
        empid = this.dataset.empid;
        action = this.dataset.action;
        console.log(empid);
        let url = '/emp-approve';
        fetch(url,{
          method:'POST',
          headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          body:JSON.stringify({'action':action,'empid':empid})
          })
          .then((response)=>{
            return response.json()
          })
          .then((data)=>{
            document.location.reload()
          })

    })
}

for(let i=0;i<viewApplicationBtn.length;i++){
  viewApplicationBtn[i].addEventListener('click',function(){
    applicationModal[i].style.display="block";
    appCloseBtn[i].addEventListener('click',()=>applicationModal[i].style.display= "none");
    window.addEventListener('click',function(e){
      if (e.target==applicationModal[i]){
        applicationModal[i].style.display = 'none';
      }
    })
  })
}
