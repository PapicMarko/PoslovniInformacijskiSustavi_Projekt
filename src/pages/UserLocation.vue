<template>
    <div>
        <section class="ui two column centered grid" style="position:relative; z-index:1;">
            <div class="column green">
                <form class="ui segment large form">
                    <div class="ui message red" v-show="error">{{error}}</div>
                    <div class="ui segment">
                        <div class="field">
                            <div class="ui right icon input large" :class="{loading:spinner}">
                                <input 
                                    type="text" 
                                    placeholder="Enter your address" 
                                    v-model="address"
                                    id="autocomplete" 
                                />
                                <i class="dot circle link icon" @click="locatorButtonPressed"></i>
                        </div>
                        </div>
                    </div>
                    <button class="ui button" @click="showUserLocationOnTheMap">POKAŽI</button>
                </form>
            </div>            
        </section>
        <section id="map"></section>
    </div>
</template>


<script>
import axios from 'axios'
var pok3;
var pok4;
export default {
    data(){
        return {
            address: "",
            error: "",
            spinner: false,          
        };
    },

    
    
    methods : {

        getAddressFrom(lat, long) {
            axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long + "&key=AIzaSyCc_CY_DWbBD8xWnZALfvX2Fhi8vTpvZes")
            .then(response => {
                if(response.data.error_message){
                    this.error=response.data.error_message;
                    console.log(response.data.error_message);
                } else {
                    this.address=response.data.results[0].formatted_address
                    console.log(response.data.results[0].formatted_address);
                }
                this.spinner=false;
            })
            .catch(error => {
                this.error= error.message;
                this.spinner=false;
                console.log(error.message);
            })

        },
                        

        locatorButtonPressed() {

            this.spinner=true;
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => {
                        //console.log(position.coords.latitude),
                        //console.log(position.coords.longitude),
                        position.coords.latitude,
                        position.coords.longitude,
                        //pok3 = position.coords.latitude,
                        //pok4 = position.coords.longitude,
                        console.log(this.pok1)
                        //console.log(this.pok2)
                        //console.log(this.pok3)
                        //console.log(this.pok4)
                        this.getAddressFrom(
                            position.coords.latitude,
                            position.coords.longitude
                        );
                        this.showUserLocationOnTheMap(position.coords.latitude, position.coords.longitude)
                    },

                    
                    error => {
                        this.error="Molim Vas upišite adresu.";
                        this.spinner=false;
                        console.log(error.message);
                    },
                );
            } else {
                this.error=error.message;
                this.spinner=false;
                console.log("Your browser does not support geolocation API");
            }

        },

/*         getAddressFrom(lat, long) {
            axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long + "&key=AIzaSyCc_CY_DWbBD8xWnZALfvX2Fhi8vTpvZes")
            .then(response => {
                if(response.data.error_message){
                    this.error=response.data.error_message;
                    console.log(response.data.error_message);

                } else {
                    this.address=response.data.results[0].formatted_address
                    console.log(response.data.results[0].formatted_address);
                   

                }
                this.spinner=false;
            })
            .catch(error => {
                this.error= error.message;
                this.spinner=false;
                console.log(error.message);
            })

        }, */

/*         mounted() {
        new google.maps.places.Autocomplete(
            document.getElementById("autocomplete"),
                {
                bounds: new google.maps.LatLngBounds(
                    new google.maps.LatLng(44.86833, 13.84806)
                    )
                }    
            )
        }, */

        showUserLocationOnTheMap(latitude, longitude, google) {
/*             pok3=pok1
            pok4=this.pok2; */
            let map = new google.maps.Map(document.getElementById("map"),  {
                zoom: 15,
                center: new google.maps.LatLng(latitude,longitude),
                mapTypeId: google.maps.MapTypeId.ROADMAP    
            });
        } 
    }
};
</script>
<style>
.ui.button,
.dot.circle.icon {
    background-color: #c3d618;
    color: white;
}

.pac-icon{
    display:none;
}

.pac-item{
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
}

.pac-item:hover {
    background-color: cadetblue;
}

.pac-item-quary {
    font-size: 16px;
}


#map {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(255, 255, 255, 0.767);
}

</style>