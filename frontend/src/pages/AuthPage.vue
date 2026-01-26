<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { login } from '@/api/auth'
import { tokenName } from '@/api/http'

const router = useRouter()
const route = useRoute()

const username = ref('')
const password = ref('')
const isLoading = ref(false)
const error = ref('')

const handleLogin = async () => {
  if (!username.value || !password.value) {
    error.value = 'Заполните все поля'
    return
  }

  isLoading.value = true
  error.value = ''

  try {
    const response = await login({
      username: username.value,
      password: password.value,
    })

    // Успех
    const token = response.data.token
    localStorage.setItem(tokenName, token)
    const redirectPath = (route.query.redirect as string) || '/'
    router.push(redirectPath)
  } catch (err: any) {
    console.error(err)

    // ОЧИСТКА ПАРОЛЯ ПРИ ОШИБКЕ
    username.value = ''
    password.value = ''
    // Логин можно оставить, чтобы юзер не вводил заново

    // Обработка текста ошибки
    if (err.response?.status === 400) {
      error.value = 'Неверный логин или пароль'
    } else if (err.response?.status === 403) {
      error.value = 'Доступ запрещен (403). Проверьте права.'
    } else {
      error.value = 'Ошибка сервера. Попробуйте позже.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="bg-dark-surface p-8 rounded-2xl border border-white/5 shadow-xl w-full">
    <h2 class="text-xl font-bold text-center mb-6">Вход в систему</h2>

    <form @submit.prevent="handleLogin" class="space-y-4">
      <!-- Логин -->
      <div>
        <label class="block text-xs text-dark-muted mb-1 ml-1">Логин</label>
        <input
          v-model="username"
          type="text"
          class="w-full bg-dark-bg border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition-colors"
          placeholder="user"
        />
      </div>

      <!-- Пароль -->
      <div>
        <label class="block text-xs text-dark-muted mb-1 ml-1">Пароль</label>
        <input
          v-model="password"
          type="password"
          class="w-full bg-dark-bg border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-primary transition-colors"
          placeholder="••••••"
        />
      </div>

      <!-- Ошибка -->
      <div v-if="error" class="text-red-400 text-sm text-center">
        {{ error }}
      </div>

      <!-- Кнопка -->
      <button
        type="submit"
        :disabled="isLoading"
        class="w-full bg-primary hover:bg-primary-hover text-white font-bold py-3.5 rounded-xl transition-all active:scale-[0.98] disabled:opacity-50 disabled:cursor-not-allowed mt-4"
      >
        <span v-if="isLoading">Входим...</span>
        <span v-else>Войти</span>
      </button>
    </form>
  </div>
</template>
