import streamlit as st
import base64

st.title("elena site!!!")

st.header("Clean Water")
text = """
This is a game called "Clean Water" where it is based on the SDG #6 called, "Clean Water and Sanitation". This is meant to represent
the idea of cleaning water and people doing that action. You can play this game by clicking on all the dirty trash in the water and 
making the water clean. However, the more levels you play, the harder it gets for clicking the trash. At the end, there is an ending 
slide for a suprise! c: 
"""
st.write(text)

# Function to convert an image file to a base64 encoded string.
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to the image files.
image_path_1 = "1.png"
image_path_2 = "2.png"
image_path_clean = "clean.png"
image_path_6 = "6.png"

# Encode images.
encoded_image_1 = get_base64_image(image_path_1)
encoded_image_2 = get_base64_image(image_path_2)
encoded_image_clean = get_base64_image(image_path_clean)
encoded_image_6 = get_base64_image(image_path_6)

# HTML/JavaScript code for interaction
html_code = f"""
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {{
      position: relative;
      display: inline-block;
    }}
    .clickable-area {{
      position: absolute;
      cursor: pointer;
      background-color: transparent;
      top: 240px;
      left: 230px;
      width: 145px;
      height: 50px;
      border: none;
    }}
  </style>
</head>
<body>
  <div class="container" id="imageContainer">
    <img id="image" src="data:image/png;base64,{encoded_image_1}" width="600">
    <div id="initialBox" class="clickable-area" onclick="onFirstClick()"></div>
  </div>

  <script>
    function onFirstClick() {{
      document.getElementById("image").src = "data:image/png;base64,{encoded_image_2}";
      document.getElementById("initialBox").remove();

      const positions = [
        {{ top: 170, left: 520, width: 30, height: 30 }},
        {{ top: 179, left: 50, width: 55, height: 55 }},
        {{ top: 173, left: 227, width: 65, height: 57 }},
        {{ top: 240, left: 110, width: 70, height: 60 }},
        {{ top: 250, left: 215, width: 80, height: 60 }},
        {{ top: 250, left: 340, width: 60, height: 50 }},
        {{ top: 200, left: 410, width: 50, height: 60 }}
      ];

      const container = document.getElementById("imageContainer");
      const cleanImageSrc = "data:image/png;base64,{encoded_image_clean}";
      const finalImageSrc = "data:image/png;base64,{encoded_image_6}";
      let cleanedCount = 0;

      positions.forEach((pos) => {{
        const div = document.createElement("div");
        div.className = "clickable-area";
        div.style.top = pos.top + "px";
        div.style.left = pos.left + "px";
        div.style.width = pos.width + "px";
        div.style.height = pos.height + "px";

        div.onclick = function () {{
          const img = document.createElement("img");
          img.src = cleanImageSrc;
          img.className = "clean-img";
          img.style.position = "absolute";
          img.style.top = pos.top + "px";
          img.style.left = pos.left + "px";
          img.style.width = pos.width + "px";
          img.style.height = pos.height + "px";
          container.appendChild(img);
          div.remove();

          cleanedCount++;
          if (cleanedCount === 7) {{
            document.querySelectorAll(".clean-img").forEach(el => el.remove());
            document.getElementById("image").src = finalImageSrc;

            positionsFor3.forEach((pos, index) => {{
              const div = document.createElement("div");
              div.className = "clickable-area";
              div.style.top = pos.top + "px";
              div.style.left = pos.left + "px";
              div.style.width = pos.width + "px";
              div.style.height = pos.height + "px";
              div.style.border = "2px solid red";
              div.onclick = function() {{
                alert(`You clicked red box #${{index + 1}} on 3.png`);
              }};
              container.appendChild(div);
            }});
          }}
        }};
        container.appendChild(div);
      }});
    }}
  </script>
</body>
</html>
"""

# Render the custom HTML code within the Streamlit app.
st.components.v1.html(html_code, height=700)
