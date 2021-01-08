<script lang="ts">
    import { onMount } from "svelte";

    onMount(() => {
        // document.querySelectorAll("pre code").forEach((el) => {
        //     hljs.highlightBlock(el as HTMLElement);
        // });

        document
            .querySelector("#copy-code")
            .addEventListener("click", copyPipInstallCommand);
    });

    function copyPipInstallCommand() {
        if (!document) return;

        const codeEl = document.getElementById("copy-code");
        const original = codeEl.innerText;

        const input = document.createElement("input");
        input.value = "pip install donttrust";
        document.body.appendChild(input);
        input.select();
        document.execCommand("copy");
        input.remove();

        codeEl.innerText = "Copied!";

        setTimeout(() => (codeEl.innerText = original), 2500);
    }
</script>

<svelte:head>
    <title>DontTrust Docs</title>
</svelte:head>

<div
    class="w3-light-gray w3-border-bottom w3-border-black w3-container w3-center"
    style="padding: 5rem 1rem">
    <h1 class="w3-xxxlarge w3-center">DontTrust</h1>
    <code
        class="w3-border w3-center w3-white w3-border-black w3-padding"
        style="cursor: pointer;"
        id="copy-code">$ pip install donttrust</code>
    <p class="w3-center w3-large w3-text-dark-gray">
        Form validation for python
    </p>

    <p>
        <a
            class="w3-center w3-button w3-blue w3-hover-blue w3-hover-text-light-gray w3-round-xxlarge"
            href="/docs">Read the docs</a>
        <a
            href="https://github.com/arnu515/donttrust"
            class="w3-center w3-button w3-dark-gray w3-round-xxlarge">Github</a>
    </p>
</div>

<div class="w3-border-bottom w3-border-black w3-container">
    <h2 class="w3-center w3-xlarge">Easy to use API</h2>

    <div class="w3-row-padding">
        <div class="w3-col m6">
            <pre><code
                    class="language-python">
from donttrust import DontTrust, Schema

trust = DontTrust(username=Schema().string().required().strip().min(4).max(16).regex(r"[\w_]+"),
                  password=Schema().string().required().min(8),
                  email=Schema().email().required().allow_mail_providers("gmail", "outlook"),
                  promotions=Schema().boolean().default(False))

print(trust.validate_and_return_json_object({'{"username": "  test    ", "password": "password1", "email": "test@gmail.com"'}))
            </code></pre>
        </div>

        <pre class="w3-col m6"><code class="language-json">
// OUTPUT:
{`{
    "username": "test",
    "password": "password1",
    "email": "test@gmail.com"
}`}
            </code></pre>
    </div>
</div>

<div class="w3-border-bottom w3-border-black w3-container">
    <h2 class="w3-center w3-xlarge">Use with any framework</h2>

    <pre><code
            class="language-python">
# Flask in this example

from flask import Flask, request, make_response, jsonify
from donttrust import DontTrust, Schema, ValidationError

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login_route():
    trust = DontTrust(username=Schema().string().required().strip().alphanum().min(4).max(32),
                      password=Schema().string().required().min(8),
                      remember_me=Schema().boolean().default(True))
    
    # Assuming request.form has the fields username, password and optionally, remember_me:
    try:
        return make_response(jsonify(trust.validate(request.form)))
    except ValidationError as e:
        return make_response(jsonify({`{"field": e.field, "message": e.message}`}), 400)

if __name__ == "__main__":
    app.run()
    </code></pre>
</div>
