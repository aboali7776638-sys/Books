from typing import List, Optional, Union
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def get_main_menu_keyboard(is_admin: bool = False) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text="📚 المكتبة"), KeyboardButton(text="🔍 بحث"))
    builder.row(KeyboardButton(text="❤️ المفضلة"), KeyboardButton(text="📥 سجل التحميلات"))
    builder.row(KeyboardButton(text="👤 الملف الشخصي"), KeyboardButton(text="⚙️ الإعدادات"))
    if is_admin:
        builder.row(KeyboardButton(text="👑 لوحة تحكم المالك"))
    return builder.as_markup(resize_keyboard=True)

def get_admin_keyboard_enhanced() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📊 إحصائيات متقدمة", callback_data="admin_stats"))
    builder.row(InlineKeyboardButton(text="📚 إدارة الكتب", callback_data="admin_books"))
    builder.row(InlineKeyboardButton(text="📁 إدارة الأقسام", callback_data="admin_categories"),
                InlineKeyboardButton(text="✍️ إدارة المؤلفين", callback_data="admin_authors"))
    builder.row(InlineKeyboardButton(text="📡 قنوات الإجبار", callback_data="admin_channels"),
                InlineKeyboardButton(text="🚫 إدارة المستخدمين", callback_data="admin_users"))
    builder.row(InlineKeyboardButton(text="🏪 إدارة السوق", callback_data="admin_market"),
                InlineKeyboardButton(text="🏆 إدارة التحديات", callback_data="admin_challenges"))
    builder.row(InlineKeyboardButton(text="🤖 مساعد AI", callback_data="admin_ai"),
                InlineKeyboardButton(text="🔒 الأمان والتدقيق", callback_data="admin_security"))
    builder.row(InlineKeyboardButton(text="🔔 إدارة الإشعارات", callback_data="admin_notifications"),
                InlineKeyboardButton(text="🎯 إدارة الإحالات", callback_data="admin_referral"))
    builder.row(InlineKeyboardButton(text="📊 لوحة المتصدرين", callback_data="admin_leaderboard"))
    builder.row(InlineKeyboardButton(text="📤 رفع كتاب", callback_data="admin_upload_book"),
                InlineKeyboardButton(text="📤 تصدير CSV", callback_data="admin_export_csv"))
    builder.row(InlineKeyboardButton(text="🗑️ حذف كتاب", callback_data="admin_delete_book"))
    builder.adjust(2)
    return builder.as_markup()

def get_admin_books_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ إضافة كتاب", callback_data="admin_upload_book"))
    builder.row(InlineKeyboardButton(text="📋 عرض الكتب", callback_data="admin_book_list"))
    builder.row(InlineKeyboardButton(text="⏳ كتب قيد المراجعة", callback_data="admin_pending_books"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    builder.adjust(1)
    return builder.as_markup()

def get_admin_categories_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ إضافة قسم جديد", callback_data="admin_add_category"))
    builder.row(InlineKeyboardButton(text="📋 عرض جميع الأقسام", callback_data="admin_cat_list"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    builder.adjust(1)
    return builder.as_markup()

def get_admin_authors_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ إضافة مؤلف", callback_data="admin_add_author"))
    builder.row(InlineKeyboardButton(text="📋 عرض جميع المؤلفين", callback_data="admin_auth_list"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    builder.adjust(1)
    return builder.as_markup()

def get_admin_channels_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ إضافة قناة", callback_data="admin_add_channel"))
    builder.row(InlineKeyboardButton(text="📋 عرض القنوات", callback_data="admin_ch_list"))
    builder.row(InlineKeyboardButton(text="⚙️ إعدادات النشر", callback_data="admin_ch_settings"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    builder.adjust(1)
    return builder.as_markup()

def get_back_to_admin_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🔙 رجوع للوحة التحكم", callback_data="admin_menu"))
    return builder.as_markup()

def get_confirm_keyboard(callback_data: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅ تأكيد", callback_data=f"confirm_{callback_data}"),
        InlineKeyboardButton(text="❌ إلغاء", callback_data="admin_menu")
    )
    return builder.as_markup()

# أضف بقية الدوال المطلوبة هنا بناءً على الحاجة
def get_admin_market_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📊 إحصائيات السوق", callback_data="admin_market_stats"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    return builder.as_markup()

def get_admin_challenges_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🏆 عرض التحديات", callback_data="admin_ch_list"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    return builder.as_markup()

def get_admin_security_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📋 سجل التدقيق", callback_data="admin_audit_log"))
    builder.row(InlineKeyboardButton(text="📊 إحصائيات الأمان", callback_data="admin_security_stats"))
    builder.row(InlineKeyboardButton(text="🚫 القائمة السوداء", callback_data="admin_blacklist"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="admin_menu"))
    builder.adjust(1)
    return builder.as_markup()

def get_book_keyboard(book_id: int, is_favorite: bool = False) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📥 تحميل", callback_data=f"download_{book_id}"))
    fav_text = "❤️ إزالة من المفضلة" if is_favorite else "❤️ إضافة للمفضلة"
    builder.row(InlineKeyboardButton(text=fav_text, callback_data=f"fav_{book_id}"))
    builder.row(InlineKeyboardButton(text="⭐ تقييم", callback_data=f"rate_{book_id}"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="main_menu"))
    builder.adjust(1)
    return builder.as_markup()

def get_books_list_keyboard(books: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for book in books:
        builder.row(InlineKeyboardButton(text=book.title, callback_data=f"book_{book.id}"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="main_menu"))
    return builder.as_markup()

def get_settings_keyboard(language: str = "ar") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    lang_text = "🌐 Language: English" if language == "ar" else "🌐 اللغة: العربية"
    builder.row(InlineKeyboardButton(text=lang_text, callback_data="set_lang"))
    builder.row(InlineKeyboardButton(text="🔙 رجوع", callback_data="main_menu"))
    return builder.as_markup()

def get_rating_keyboard(book_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(1, 6):
        builder.add(InlineKeyboardButton(text="⭐" * i, callback_data=f"rate_{i}_{book_id}"))
    builder.adjust(1)
    return builder.as_markup()
