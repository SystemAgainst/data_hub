<script setup lang="ts">
import AppWidget from '@/components/ui/AppWidget.vue'

defineProps<{
  hasDocuments: boolean
}>()
</script>

<template>
  <AppWidget title="Документы" icon="📄" clickable>
    <div class="flex h-full flex-col justify-center">
      <p class="text-dark-muted text-xs">
        {{ hasDocuments ? 'Есть прикрепленные файлы' : 'Нет документов' }}
      </p>
    </div>
  </AppWidget>
</template>
