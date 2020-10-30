from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Hello)
class HelloAdmin(admin.ModelAdmin):
    pass

class PerformanceLinkInline(admin.StackedInline):
    model = PerformanceLink

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    inlines = [
        PerformanceLinkInline,
    ]

class WritingLinkInline(admin.StackedInline):
    model = WritingLink

@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    inlines = [
        WritingLinkInline,
    ]
