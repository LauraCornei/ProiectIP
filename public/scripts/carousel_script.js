const data = [
    {
        id: 0,
        name:'',
        image:'',
        description_one: '',
        description_two: ''
    },
];

const API_URL = 'http://159.65.247.164/';

const ALG_TYPES = {
    recom7: 'restaurant-by-food',
    recommend_food_for_restaurants : 'food',
    recommendations_restaurants : 'restaurant',
    restaurant_food_recommendation : 'food-for-restaurant',
}

const MEDIA_BREAKPOINTS = {
    LG: 1500,
    MD: 780,
    SM: 420,
};

window.app = new Vue({
    el: '#app',
    data: {
        window: {
            width: 0,
            height: 0,
        },
        rawData: data,
        search: '',
        slide: 0,
        sliding: null,
    },
    
    computed: {
        carouselSections: function () {
            let cardsNo = 1;
            if (this.window.width > MEDIA_BREAKPOINTS.LG) cardsNo = 4;
            else if (this.window.width > MEDIA_BREAKPOINTS.MD) cardsNo = 3;
            else if (this.window.width > MEDIA_BREAKPOINTS.SM) cardsNo = 2;
            return _.chunk(this.rawData, cardsNo);
        },
    },

    mounted: function () {
        this.$nextTick(function () {
          this.getUserIdRecomendation();
        })
      },

    created() {
        window.addEventListener('resize', this.handleResize);
        this.handleResize();
    },
    destroyed() {
        window.removeEventListener('resize', this.handleResize);
    },

    methods: {
        async getUserIdRecomendation() {
            provider_id = getParamValue('provider_id'); 
            token = getParamValue('token');
            alg_type = getParamValue('alg_type');

            const recommendationsArray = await this.getRecommedations(token, provider_id, alg_type);
            console.log(recommendationsArray.success);
            if(provider_id && recommendationsArray.success != 'false'){
                this.rawData = recommendationsArray.data.map(e => {
                    return e[0];
                }
                ).map(e => {
                    if(e.category != null && e.image != null)
                        return {
                            ...e,
                            name: e.name,
                            image: e.image,
                            description_one: "Category: " + e.category[0],
                            description_two: "Price: " + e.price
                        }
                    else if(e.category == null && e.image != null)
                        return {
                            ...e,
                            name: e.name,
                            image: e.image,
                            description_one: "Price: " + e.price
                        }
                    else if(e.category != null && e.image == null){
                         return{
                            ...e,
                            name: e.name,
                            image: "./css/img/no_img.png",
                            description_one: "Category: " + e.category[0],
                            description_two: "Price: " + e.price
                         }
                     }
                     else 
                        return{
                            ...e,
                            name: e.name,
                            image: "./css/img/no_img.png",
                            description_two: "Price: " + e.price
                        }
                });
            }
            else if (!provider_id && recommendationsArray.success != 'false'){
                this.rawData = recommendationsArray.data.map(e => {
                    if(e.details.specials != null && e.details.images != null)
                        return {
                            ...e,
                            name: e.name,
                            image: e.details.images[0],
                            description_one: "Special: " + e.details.specials[0],
                            description_two: "Rating: " + e.details.rating
                        }

                    else if(e.details.specials != null && e.details.images == null)
                        return{
                            ...e,
                            name: e.name,
                            image: "./css/img/no_img.png",
                            description_one: "Special: " + e.details.specials[0],
                            description_two: "Rating: " + e.details.rating
                        }
                    else if(e.details.specials == null && e.details.images != null)
                        return{
                            ...e,
                            name: e.name,
                            image: e.details.images[0],
                            description_one: "Rating: " + e.details.rating
                        }
                    else if(e.details.specials == null && e.details.images == null)
                        return{
                            ...e,
                            name: e.name,
                            image: "./css/img/no_img.png",
                            description_one: "Rating: " + e.details.rating
                        }
                });
            }
            else {
                this.rawData = []; 
            }

        },

        getRecommedations(token, provider_id, alg_type) {
            console.log(alg_type);
            if(!ALG_TYPES[alg_type])
                throw new Error("alg_type not found");
            
            let path = '';
            if(provider_id)
                path += '/' + provider_id;
              
            
            return fetch(
                `${API_URL}recommendations/${ALG_TYPES[alg_type]}${path}` , {headers:{Authorization:'Bearer ' + token}}
            ).then((res) => res.json());
        },

        handleResize() {
            this.window.width = window.innerWidth;
            this.window.height = window.innerHeight;
        },

        onSlideStart(slide) {
            this.sliding = true;
        },
        onSlideEnd(slide) {
            this.sliding = false;
        },
    },
});
