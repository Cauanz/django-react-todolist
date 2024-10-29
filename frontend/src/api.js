import axios from 'axios'
import { ACCESS_TOKEN } from './constants'

//* CRIA UMA INSTANCIA DO AXIOS COM UMA URL BASE PARA ONDE TODAS AS REQUISIÇÕES SERÃO FEITAS, ELE SÓ FAZ REQUISIÇÕES SE UM TOKEN ESTIVER PRESENTE

const api = axios.create({
   baseURL: import.meta.env.VITE_API_URL
})

api.interceptors.request.use(
   (config) => {
      const token = localStorage.getItem(ACCESS_TOKEN)
      if(token){
         config.headers.Authorization = `Bearer ${token}`
      }
      return config
   },
   (error) => {
      return Promise.reject(error)
   }
)

export default api