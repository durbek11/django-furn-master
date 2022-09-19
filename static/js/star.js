let rate_text = document.querySelectorAll(".feature-review")

rate_text.forEach((item)=>{
    let stars = item.parentNode.querySelectorAll('.star')
    stars.forEach((star)=>{
        for (let i = 0; i < item.textContent; i++){
            stars[i].classList.remove("gray")
        }
    })
})
