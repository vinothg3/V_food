var profile_data=document.querySelector("#profile_data");
var dbtn=document.getElementById("btn");


function ProfileToggle()
{
    profile_data.classList.toggle('pro_data');

}
dbtn.onclick=function()
{
    dbtn.classList.toggle("btn-on")
}