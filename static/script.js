/*
--------------------------------------------------
Hybrid AI Vitamin Chatbot
Frontend JavaScript
--------------------------------------------------
*/

const chatContainer = document.getElementById("chat-container");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");


function addMessage(sender, message, metadata = null) {

    const wrapper = document.createElement("div");
    wrapper.className = `message ${sender}`;

    const content = document.createElement("div");
    content.className = "message-content";

    content.innerHTML = message.replace(/\n/g, "<br>");

    if (metadata) {

        const info = document.createElement("div");

        info.style.marginTop = "10px";
        info.style.fontSize = "12px";
        info.style.color = "#666";

        info.innerHTML =
            `<strong>Source:</strong> ${metadata.source}
            &nbsp; | &nbsp;
            <strong>Model:</strong> ${metadata.model}
            &nbsp; | &nbsp;
            <strong>Time:</strong> ${metadata.processing_time_ms} ms`;

        content.appendChild(info);
    }

    wrapper.appendChild(content);

    chatContainer.appendChild(wrapper);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}


async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "")
        return;

    addMessage("user", message);

    userInput.value = "";

    sendButton.disabled = true;

    const thinking = document.createElement("div");
    thinking.className = "message bot";
    thinking.id = "thinking";

    thinking.innerHTML =
        `<div class="message-content">
            🤖 Thinking...
        </div>`;

    chatContainer.appendChild(thinking);

    chatContainer.scrollTop = chatContainer.scrollHeight;

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        thinking.remove();

        if (data.success) {

            addMessage(
                "bot",
                data.response,
                {
                    source: data.source,
                    model: data.model,
                    processing_time_ms: data.processing_time_ms
                }
            );

        }
        else {

            addMessage(
                "bot",
                "❌ " + data.error
            );

        }

    }
    catch (error) {

        thinking.remove();

        addMessage(
            "bot",
            "Unable to connect to the server."
        );

        console.error(error);

    }

    sendButton.disabled = false;

    userInput.focus();
}


sendButton.addEventListener(
    "click",
    sendMessage
);


userInput.addEventListener(
    "keypress",
    function (event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);


userInput.focus();
