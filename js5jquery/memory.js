var cards = ["ciri.png","geralt.png","jaskier.png","jaskier.png","iorweth.png","triss.png","geralt.png","yen.png","ciri.png","triss.png","yen.png","iorweth.png"]

//alert(cards[3]);

//console.log(cards);

var c0 = document.getElementById('c0');
var c1 = document.getElementById('c1');
var c2 = document.getElementById('c2');
var c3 = document.getElementById('c3');
var c4 = document.getElementById('c4');
var c5 = document.getElementById('c5');
var c6 = document.getElementById('c6');
var c7 = document.getElementById('c7');
var c8 = document.getElementById('c8');
var c9 = document.getElementById('c9');
var c10 = document.getElementById('c10');
var c11= document.getElementById('c11');


c0.addEventListener("click", function() { revealCard(0); });
c1.addEventListener("click", function() { revealCard(1); });
c2.addEventListener("click", function() { revealCard(2); });
c3.addEventListener("click", function() { revealCard(3); });
c4.addEventListener("click", function() { revealCard(4); });
c5.addEventListener("click", function() { revealCard(5); });
c6.addEventListener("click", function() { revealCard(6); });
c7.addEventListener("click", function() { revealCard(7); });
c8.addEventListener("click", function() { revealCard(8); });
c9.addEventListener("click", function() { revealCard(9); });
c10.addEventListener("click", function() { revealCard(10); });
c11.addEventListener("click", function() { revealCard(11); });

var oneVisible = false;
var turnCounter = 0;
var visible_nr;
var lock = false; // so that you cant click too fast on divs
var pairsleft = 6;

function revealCard(nr)
{
	var opacityValue = $('#c'+nr).css('opacity'); // variable to not go to another turn just by clicking element with 0 opacity

	if(opacityValue != 0 && lock == false) // if this wont work, no futher action avaiable
	{

		lock = true;
		var obraz = "url(img/"+cards[nr]+")";
		$('#c'+nr).css('background-image', obraz); //zlapanie i podmiana
		$('#c'+nr).addClass('cardA');
		$('#c'+nr).removeClass('card');

		if(oneVisible == false)
		{
			//first card
			oneVisible = true; //one card is up
			visible_nr = nr; // saving which card is up so we can check if the second one (the same) was picked
			lock = false;
		}
		else
		{
			//second card

			if(cards[visible_nr] == cards[nr]) //found pair
			{
				setTimeout(function() { hide2Cards(nr, visible_nr)}, 750); //activates the function after 750 miliseconds
			}
			else //miss
			{
				
				setTimeout(function() { restore2Cards(nr, visible_nr)}, 1000); //activates the function after 750 miliseconds
			}

			turnCounter++; 
			$('.score').html('Turn counter: '+turnCounter); //put the number of turns on the screen by changing inner html of class score usng jQuery
			oneVisible = false; //change it to false again, reset
		}
	}
}



function hide2Cards(nr1, nr2)
{
	$('#c'+nr1).css('opacity', '0'); //catch the first element, change it css property opacity to 0 (hide it)
	$('#c'+nr2).css('opacity', '0'); //second
	pairsleft--;

	if(pairsleft == 0)
	{
		$('.board').html('You win!. Done in: ' +turnCounter+ ' rounds.');
	}

	lock = false;
}

function restore2Cards(nr1, nr2)
{
	$('#c'+nr1).css('background-image', 'url(img/karta.png)'); //zlapanie i podmiana
	$('#c'+nr1).addClass('card');
	$('#c'+nr1).removeClass('cardA');

	$('#c'+nr2).css('background-image', 'url(img/karta.png)'); //zlapanie i podmiana
	$('#c'+nr2).addClass('card');
	$('#c'+nr2).removeClass('cardA');

	lock = false;
}