<template>
    <section class="ui two column centered grid">
        <div class="column red">
            <form class="ui segment large form">
                <div class="ui message red" v-show="error">{{error}}</div>
                <div class="ui segment"></div>
                    <div class="field">
                       <div class="ui right icon input large" :class="{loading:spinner}">
                            <input type="text" placeholder="Enter your address" v-model="address" />
                            <i class="dot circle link icon" @click="locatorButtonPressed"></i>
                       </div>
                    </div>
                    <button class="ui button">GO</button>
            </form>
        </div>
    </section>
</template>


<script>

import axios from 'axios'

export default {

    data(){
        return {
            address: "",
            error: "",
            spinner: false
        }
    },

    methods : {
        locatorButtonPressed() {

            this.spinner=true;
            if(navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    position => {
                        this.getAddressFrom(position.coords.latitude, position.coords.longitude)
        
                    },
                    error => {
                        this.error="Molim Vas upišite adresu manualno";
                        this.spinner=false;
                        //console.log(error.message);
                    }
                );
            } else {
                this.error=error.message;
                this.spinner=false;
                console.log("Your browser does not support geolocation API");
            }

        },

        getAddressFrom(lat, long) {
            axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long + "&key=AIzaSyCc_CY_DWbBD8xWnZALfvX2Fhi8vTpvZes")
            .then(response => {
                if(response.data.error_message){
                    this.error=response.data.error_message;
                    console.log(response.data.error_message);
                } else {
                    this.address=response.data.results[0].formatted_address
                    //console.log(response.data.results[0].formatted_address);
                }
                this.spinner=false;
            })
            .catch(error => {
                this.error= error.message;
                this.spinner=false;
                console.log(error.message);
            })

        }
    }
}
</script>
<style>
.ui.button,
.dot.circle.icon {
    background-color: #ff5a5f;
    color: white;
}
</style>
