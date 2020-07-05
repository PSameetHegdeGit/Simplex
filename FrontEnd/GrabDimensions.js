
document.querySelector('.submit').addEventListener('click', grabVariables)


function grabVariables(e){

    noOfVariables = document.querySelector('#noOfVariables').value
    
    sessionStorage.setItem("noOfVariables", noOfVariables)

    e.preventDefault()

    setTimeout(function(){
        let url = './simplex_dimensions.html'  
        window.location = url
    }, 20)
}





