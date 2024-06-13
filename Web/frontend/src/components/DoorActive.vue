<template>
    <v-container style="align-items: center;">
        <div>
            <h3>{{ message }}</h3>
            <div>
                <v-btn @click="OpenGate" v-if="isUser">출입문 open</v-btn><br>
            </div>
            <div style = "margin-top: 5%;">
                <img v-if="imageSrc" :src="imageSrc" alt="이미지 미리보기" height="300px" width="300px" />
            </div>
        </div>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            urlinfo: "http://192.168.137.7:5000/door",
            message: "손님 대기중...",
            isUser: false,
            imageSrc: null
        };
    },
    created() {
        this.$socket.on('live', (data) => {
            this.isUser = true;
            this.message = "새로운 출입요청! 체온: " + data.temperature;
        });

        this.$socket.on('image', (data) => {
            // 서버로부터 받은 이미지 경로를 img 태그의 src에 바인딩
            if (data.filePath) {
                this.imageSrc = `http://localhost:8000${data.filePath}`;
            }
            else{
                this.imageSrc = null;
            }
        });
    },
    methods: {
        OpenGate() {
            axios.get(this.urlinfo)
                .then(() => {
                    console.log("게이트 open");
                    setTimeout(() => {
                        this.message = "손님 대기중...";
                        this.isUser = false;
                        this.imageSrc = null;
                    }, 3000);
                })
                .catch((err) => {
                    alert("에러 발생: ", err);
                });
        }
    }
};
</script>