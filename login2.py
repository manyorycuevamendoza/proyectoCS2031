{
    <form action="" method="post" novalidate>
    {{ form.hidden_tag() }}
    <p>
        {{ form.username.label }}<br>
        {{ form.username(size=32) }}
        {% for error in form.username.errors %}
        <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>
        {{ form.password.label }}<br>
        {{ form.password(size=32) }}
        {% for error in form.password.errors %}
        <span style="color: red;">[{{ error }}]</span>
        {% endfor %}
    </p>
    <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
    <p>{{ form.submit() }}</p>
</form>
#}