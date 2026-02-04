const para = document.createElement("p")
para.textContent = "this is a paragraph";
console.log(para);
document.getElementById("content").appendChild(para)

document.querySelector("#content p").remove();


const image =document.createElement("img");
image.setAttribute("src","https://www.bing.com/images/search?view=detailV2&ccid=mbTKQLNR&id=D4413619B5BACF5CE591F68AB1CD0706BA394A9D&thid=OIP.mbTKQLNRv_COBwBSWaEknAHaHB&mediaurl=https%3A%2F%2Fimages.sftcdn.net%2Fimages%2Ft_app-cover-l%2Cf_auto%2Fp%2F05cce3ac-96d8-11e6-950e-00163ed833e7%2F2099543107%2Ffast-image-resizer-screenshot.jpg&exph=968&expw=1020&q=image+resizer&FORM=IRPRST&ck=F7DD269ECEF88D37A710383209BCB1C8&selectedIndex=2&itb=0&cw=718&ch=567&ajaxhist=0&ajaxserp=0");

image.setAttribute("alt","java");
const gallery=document.getElementById("gallery");
gallery.appendChild(image)