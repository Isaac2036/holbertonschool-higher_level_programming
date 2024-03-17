const myList = document.querySelector('.my_list');
const addItem = document.getElementById('add_item');
const removeItem = document.getElementById('remove_item');
const clearList = document.getElementById('clear_list');

addItem.addEventListener('click', function() {
  const li = document.createElement('li');
  li.textContent = 'Item';
  myList.appendChild(li);
});

removeItem.addEventListener('click', function() {
  if (myList.lastChild) {
    myList.removeChild(myList.lastChild);
  }
});

clearList.addEventListener('click', function() {
  while (myList.firstChild) {
    myList.removeChild(myList.firstChild);
  }
});