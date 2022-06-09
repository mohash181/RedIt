let button = document.getElementById("ccbutton");
let box = document.getElementById("changeMe");

function changeBoxColour(){
    if(box.style.background == "black"){
        box.style.background = "purple";
        console.log("purple");
    }else{
        box.style.background = "black";
        console.log("black");
    }
}