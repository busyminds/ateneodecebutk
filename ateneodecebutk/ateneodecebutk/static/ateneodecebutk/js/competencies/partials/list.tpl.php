<div class="row">
  <div class="col-md-8">
    <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title">Competency Planner</h3>
      </div>
      <div class="panel-body">
        <p>
          These competencies will be used for at least two things:
          <ol>
            <li>The <a href="ecr.php">ECR</a> will track the results of students assessments and link those results to these competencies.</li>
            <li>The <a href="http://xhimera.biz:9988">ePost</a> will use these competencies to generate the Pathway for every quarter.</li>
          </ol>
        </p>

        <p>To submit your own competencies for your classes, click the button below.</p>
        <a class="btn btn-primary btn-lg" href="#/edit"><span class="glyphicon glyphicon-check"></span> Edit Competencies</a>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="panel panel-success">
      <div class="panel-heading">
        <h3 class="panel-title">Completion Status</h3>
      </div>
      <div class="panel-body">
        <p class="lead text-center">3rd Quarter</p>
        <h1 class="text-center text-success" ng-bind="overall_status_percentage"></h1>
        <div class="progress">
          <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: {{overall_status_percentage}}">
            <span class="sr-only">{{overall_status_percentage}} Complete</span>
          </div>
        </div>
        <p class="lead text-center" ng-bind="overall_status_detail"></p>
      </div>
    </div>
  </div>
</div>

<!-- <div class="table-responsive"> -->
<div class="row">
  <div class="col-md-12">
    <h3>The following table indicates the status of each subject in each grade level.</h3>
    <div class="table-responsive">
      <table id="competencies-status" class="table">
        <thead>
          <tr>
            <th>Subject</th>
            <th>Grade 1</th>
            <th>Grade 2</th>
            <th>Grade 3</th>
            <th>Grade 4</th>
            <th>Grade 5</th>
            <th>Grade 6</th>
          </tr>
        </thead>
        <tbody>
          <tr ng-repeat="item in subject_status">
            <th>{{item.subject}}</th>
            <td ng-repeat="status in item.status" ng-class="status_int_to_class(status)">
              <a ng-href="#/edit?grade={{$index+1}}&subject={{item.subject}}" ng-class="status_int_to_class(status)" ng-show="(status != null)" tooltip-html-unsafe="{{get_subject_teachers(item.subject,$index+1)}}">
                <span ng-class="status_int_to_glyphicon(status)"></span> {{status_int_to_string(status)}}
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>