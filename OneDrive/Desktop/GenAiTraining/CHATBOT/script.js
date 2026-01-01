const chat = document.getElementById("chat")
const btn = document.querySelector("#btn")
const chatFN = async () => {
    const text_info = document.getElementById("text_info").value;
    console.log(text_info)
    chat.innerHTML += `<p><b> User: ${text_info}</b></p>`
    // api call
    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "message": text_info })
    });
    //ai 
    const data=await response.json()
    console.log(data.reply);
     chat.innerHTML += `<p><b> Bot: ${data.reply}</b></p>`
     document.getElementById("text_info").value =" ";

};
btn.addEventListener("click", chatFN);
document.getElementById("text_info").addEventListener("keydown",(e)=>{
    console.log(e);
    if (e.key=="Enter"){
        chatFN()
    }
})