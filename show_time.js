window.addEventListener("DOMContentLoaded", () => {
    const messages = document.createElement("ul");
    document.body.appendChild(messages);

    const ws = new WebSocket("ws://localhost:8765/");
    ws.onmessage = ({data}) => {
        const message = document.createElement("li");
        const content = document.createTextNode(data);
        
        message.appendChild(content);
        messages.append(message)
    };
});