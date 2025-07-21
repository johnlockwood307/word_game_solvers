const johnBtn = document.getElementById('JohnButton')
const johnTxt = document.getElementById('JohnText')

johnBtn.addEventListener('click', john)

john()

function john() {
    johnTxt.innerHTML = "John says " + Date()
}