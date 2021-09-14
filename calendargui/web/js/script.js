let date;
let dateType
getDateString = date =>`${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];



window.onload = (event) =>{
    dateType = new Date();
    date = getDateString(dateType)
    console.log(dateType);
    // clearDaylist()
}




function clearDaylist(){
    document.querySelectorAll(".day").forEach(i=>i.remove())
}
async function setDayList(s) {
    clearDaylist()
    let n = await eel.getDayList(s)();
    const container = document.getElementById("dividing_day-event")
    n.forEach(element =>{
        const newDay = document.createElement("div")
        newDay.classList = `${element[1]}`
        newDay.innerText=`${element[0]}`
        newDay.id=element[2]
        console.log(element[0]);
        document.getElementById("calendar").insertBefore(newDay,container)
    });
    document.getElementById("year").textContent = dateType.getFullYear()
    document.getElementById("month").textContent = monthNames[dateType.getMonth()]
}




btn = document.getElementById("btn")
btn.addEventListener("click",()=>{
    console.log(date);
    setDayList(date)
});

btn = document.getElementById("btn2")
btn.addEventListener("click",clearDaylist)




function menu(){
    
    document.getElementById("option").style.display ="grid"
    document.getElementById("overlay").style.display = "block"
    // eel.printtext("a.innerText");
}

function x(){
    console.log("cls");
    document.getElementById("option").style.display ="none"
    document.getElementById("overlay").style.display = "none"
}

function selectedM(a){
    dateType.setMonth(monthNames.indexOf(a.innerText))
    dateType.setDate(1)
    date = getDateString(dateType)
    console.log(date);
    document.getElementById("smonthActive").id="smonth"
    a.id = "smonthActive"
    setDayList(date)
}
function selectedY(a){
    dateType.setFullYear(parseInt(a.innerText))    
    dateType.setDate(1)
    date = getDateString(dateType)
    console.log(date);    
    document.getElementById("syearActive").id="syear"
    a.id = "syearActive"
    setDayList(date)
}