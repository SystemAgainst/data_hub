<script setup lang="ts">
import AppWidget from '@/components/ui/AppWidget.vue'
import type { UserMini } from '@/types'

const props = defineProps<{
  participants?: UserMini[]
}>()
</script>

<template>
  <AppWidget title="Команда" icon="👥" :badge="props.participants?.length || 0">
    <!-- Контент: Список людей -->
    <div v-if="participants && participants.length > 0" class="flex flex-wrap gap-2">
      <div
        v-for="user in participants"
        :key="user.id"
        class="flex items-center gap-2 rounded-lg bg-white/5 px-3 py-1.5"
        :title="user.username"
      >
        <div
          class="bg-primary/20 text-primary flex h-6 w-6 items-center justify-center rounded-full text-xs font-bold uppercase"
        >
          {{ user.first_name?.[0] || user.username[0] }}
        </div>
        <span class="text-sm text-gray-200">
          {{ user.first_name || user.username }}
        </span>
      </div>
    </div>

    <div v-else class="text-dark-muted py-2 text-center text-sm">Нет участников</div>
  </AppWidget>
</template>
