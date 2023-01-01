console.log("tested")

window.addEventListener('DOMContentLoaded',()=>{

    let menu_btn=document.getElementById('menu')
    let menus=document.getElementById('menubar')
    menu_btn.addEventListener('click' ,()=>{
       menus.classList.toggle('left-[0px]')
       menus.classList.toggle('bg-blue-500')
       menus.classList.toggle('text-white')
    
    })
})

let username=document.getElementById('id_username')
let min=document.getElementById('min')
let tick=document.getElementById('tick')
username.addEventListener('input',()=>{
    if(username.value.length > 4){
        min.style.color="green"
        tick.style.opacity="1"
    }
    else{
        min.style.opacity="1"
        min.style.color="red"
        tick.style.opacity="0"

    }
})

let email=document.getElementById('id_email')
let text=document.getElementById('text')
let em=document.getElementById('em')
email.addEventListener('focus',()=>{
    text.style.opacity="1"
    text.style.color="red"
    if (email.value.length > 1 && email.value.includes("@")) { 
        em.style.opacity="1"
        text.style.opacity="0"
    }
    else{
        text.style.opacity='1'
    }
})
email.addEventListener('input',()=>{
    text.style.opacity="1"
    text.style.color="red"
    if (email.value.length > 1 && email.value.includes("@")) {
        text.style.opacity="0"
        em.style.opacity="1"


    }
    else{
        text.style.opacity="1"
        em.style.opacity="0"

    }
   
})

let pass1=document.getElementById('id_password1')
let pass2=document.getElementById('id_password2')
let pas=document.getElementById('pas')
pass2.addEventListener('input',()=>{
    if(pass1.value == pass2.value){
        pas.innerHTML="Password matched.  ✔"
        pas.style.color="green"
    }
    else{
        pas.innerHTML="Password not matched.  ✔"
        pas.style.color="red"
    }
})