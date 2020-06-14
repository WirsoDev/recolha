
const ufSelect = document.querySelector('select[name=uf]')
const city = document.querySelector('select[name=city]')

function populatUfs() {
    fetch('http://www.geonames.org/childrenJSON?geonameId=2264397')
    .then( res => {return res.json()})
    .then( states => {
        c = 0
        for(let state of states.geonames){

            ufSelect.innerHTML += `<option value="${state.name}">${state.name}</option>`
            var o = document.getElementsByTagName('option')[c+1]
            o.setAttribute('id', state.geonameId)
            c ++
        }
    } )

    ufSelect.addEventListener('change', getcity)

    function getcity() {

        city.innerHTML = ''

        var x = ufSelect.selectedIndex
        var getcode = document.getElementsByTagName('option')[x]

        console.log(getcode.id)

        city.removeAttribute('disabled')

        fetch(`http://www.geonames.org/childrenJSON?geonameId=${getcode.id}`)
        .then( res => {return res.json()})
        .then( citysname => {
            c = 0
            //console.log(states.geonames)
            for(let ct of citysname.geonames){
                city.innerHTML += `<option value="${ct.toponymName}">${ct.toponymName}</option>`
                c ++
            }
        } )

    }

}



populatUfs()

