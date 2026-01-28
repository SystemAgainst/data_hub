// Описываем тип Проекта (как он приходит с бэка)
export interface Project {
  id: number
  title: string

  description?: string
  document_url?: string
  address?: string

  cover_image?: string | null

  // URLField
  google_sheet_url?: string

  // DecimalField: DRF по умолчанию отдает его как строку (String),
  // чтобы не было проблем с плавающей запятой в JS.
  // Но можно указать number, если вы уверены, что конвертируете на фронте.
  // Лучше оставить string для безопасности денег.
  total_cost?: string

  created_at: string
  updated_at: string

  // Вложенные/вычисляемые поля
  // Внимание: эти поля будут доступны ТОЛЬКО если вы добавили их в ProjectSerializer!
  // updated_by_name — это кастомное поле, его нет в БД, оно должно быть в сериалайзере.
  updated_by_name?: string

  // Если вы добавите participants в сериалайзер, то раскомментируйте:
  participants?: number[] // list of id
  participants_details?: UserMini[] // list of UserMini
}

export interface UserMini {
  id: number
  username: string
  first_name?: string
  last_name?: string
}

export interface ProjectStats {
  total_spent: string
  total_days: string
  participants: {
    name: string
    amount: string
  }[]
}
