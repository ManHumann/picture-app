const gallery = document.getElementById("gallery");

async function loadImages(){

    gallery.innerHTML = "";

    const response = await fetch("/images");
    const data = await response.json();

    data.images.forEach(filename => {

        const card = document.createElement("div");
        card.className = "card";

        card.innerHTML = `
            <img src="/images/${filename}" alt="">
            <div class="filename">${filename}</div>
            <button class="delete-btn">Delete</button>
        `;

        card.querySelector("button").onclick = async () => {

            await fetch(`/images/${filename}`,{
                method:"DELETE"
            });

            loadImages();

        };

        gallery.appendChild(card);

    });

}

document
.getElementById("uploadForm")
.addEventListener("submit", async e=>{

    e.preventDefault();

    const file =
        document.getElementById("fileInput").files[0];

    const formData = new FormData();

    formData.append("file",file);

    await fetch("/upload",{
        method:"POST",
        body:formData
    });

    document.getElementById("fileInput").value="";

    loadImages();

});

loadImages();
