document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#shorten-form");

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        
        const long_url = document.querySelector("#url-input").value;

        fetch("/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                long_url: long_url
            })
        })
        .then(response => response.json())
        .then(result => {
            if(result.error){
                document.querySelector("#error").innerHTML = `<b>Error:</b> ${result.error}`
                return
            }
            console.log(result);

            const long = result.long_url;
            const short = result.short_url;
            const clicks = result.clicks;

            document.querySelector("#error").innerHTML = ''
            document.querySelector("#long-url").innerHTML = `<b>Long Url:</b> <a href="${long}">${long}</a>`;
            document.querySelector("#short-url").innerHTML = `<b>Short Url:</b> <a href="/${short.slice(-6)}" target="_blank">${short}</a>`;
            document.querySelector("#clicks").innerHTML = `<b>No of Clicks:</b> ${clicks}`;
            document.querySelector("#url-input").value =''
        })
        .catch(err => {
            console.log(err);
        });
    });
});
