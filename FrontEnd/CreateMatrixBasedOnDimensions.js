const options = {
    greaterThanOrEqualTo: function() {
        let option = document.createElement("option")
        option.text = ">="
        option.value = ">="
        return option
    },
    lessThanOrEqualTo: function() {
        let option = document.createElement("option")
        option.text = "<="
        option.value = "<="
        return option
    },
    equalTo: function() {
        let option = document.createElement("option")
        option.text = "="
        option.value = "="
        return option
    }
}


function createMatrix(noOfVariables){
   
    let matrix = document.createElement("section")
    matrix.id = "matrix"
    
    for(let i = 1; i <= noOfVariables; i++){

        let div = document.createElement("div")
        div.className = "row"

        for(let i = 1; i <= noOfVariables; i++){
            let input = document.createElement("input")
            
            if (i != noOfVariables){
                var para = document.createTextNode(`x${i} +`)
            }
            else{
                var para = document.createTextNode(`x${i}`)
            }

            input.className = "matrix_inputs"
            div.appendChild(input)
            div.appendChild(para)
        }
        // Put in the right side of inequalities
        let select = document.createElement("select")
        select.style = "margin: 0px 20px 0px 20px;"
        select.append(options.lessThanOrEqualTo())
        select.append(options.equalTo())
        select.append(options.greaterThanOrEqualTo())
        
        div.appendChild(select)

        let rightMostInput = document.createElement("input")
        rightMostInput.className = "matrix_inputs"

        div.appendChild(rightMostInput)

        matrix.appendChild(div)
    }
    
    const submit = document.querySelector(".submit")
    document.body.insertBefore(matrix, submit)
}


try{
    var noOfVariables = parseInt(sessionStorage.getItem("noOfVariables"))
}
catch{
    console.log("Invalid entry for number of Variables ")
}


createMatrix(noOfVariables)

document.body.querySelector(".submit").addEventListener("click", () => {
    let coeffNodes = document.querySelectorAll(".matrix_inputs")
  
    matrix = []
    let counter = 0
    let row = []
    noOfRowInputs = noOfVariables + 1
   
    coeffNodes.forEach((coeffNode) =>{
             
        row.push(parseInt(coeffNode.value))
        counter++

        if(counter === noOfRowInputs){
            matrix.push(row)
            row = []
            counter = 0

        }
    })

    console.log(matrix)
})