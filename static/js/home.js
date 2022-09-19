let btns = document.querySelectorAll('button')

btns.forEach((btn)=>{
    btn.addEventListener('click', ()=>{
        setTimeout(()=>{
            document.location.href = "/"
        }, 3000)
    })
})

