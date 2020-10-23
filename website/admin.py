from django.contrib import admin

from .models import *

# Register your models here.

class HelloLinkInline(admin.StackedInline):
    model = HelloLink

@admin.register(Hello)
class HelloAdmin(admin.ModelAdmin):
    inlines = [
        HelloLinkInline,
    ]

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
